import subprocess,sys,json,hashlib,signal,time,datetime
from pathlib import Path
repo=Path('/content/commandmed-source')
RUN_HEAD='848692336c2b8537ee4d559338abed29da0c93d6'
assert subprocess.check_output(['git','-C',str(repo),'rev-parse','HEAD'],text=True).strip()==RUN_HEAD
admission={'cost_basis':'COLAB_FREE_EXPOSED_RESOURCES','ui_subscription':'NOT_SUBSCRIBED','compute_unit_balance':0,'expected_incremental_spend_usd':0,'new_purchase':False,'normal_interactive_notebook':True,'notebook_id':'1RfTpKjRAfqamgTWrw1j3pM4eAKzZScY4','observed_remaining_runtime_seconds':9600,'ui_reported_window_seconds':10200,'conservative_admission_buffer_seconds':600,'observed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'notebook_template_sha256':hashlib.sha256((repo/'notebooks/v5_s1_colab_resource_qualification.ipynb').read_bytes()).hexdigest(),'new_runtime_after_operational_disconnect':True,'resume':False,'reconnection_record_sha256':hashlib.sha256(Path('/content/commandmed-reconnection.json').read_bytes()).hexdigest(),'launch_source_sha256':LAUNCH_SOURCE_SHA256}
admission['cpu_model']=next((line.split(':',1)[1].strip() for line in Path('/proc/cpuinfo').read_text().splitlines() if line.startswith('model name')),'UNAVAILABLE')
Path('/content/commandmed-b1-admission.json').write_text(json.dumps(admission,indent=2)+'\n')
command=[sys.executable,'-u','-B',str(repo/'scripts/v5_s1_b1_development.py'),'--expected-head',RUN_HEAD,'--model-dir','/content/commandmed-model','--source','/content/riskcalcs.json','--admission','/content/commandmed-b1-admission.json']
log=Path('/content/commandmed-b1-console.log')
with log.open('w') as console:
    child=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)
    try:
        for line in child.stdout:
            console.write(line); console.flush(); print(line,end='',flush=True)
        exit_code=child.wait()
    except KeyboardInterrupt:
        child.send_signal(signal.SIGINT)
        try: tail,_=child.communicate(timeout=45)
        except subprocess.TimeoutExpired:
            child.terminate(); tail,_=child.communicate(timeout=15)
        console.write(tail or ''); console.flush(); print(tail or '',end='',flush=True)
        exit_code=child.returncode
        print('FOREGROUND_CHILD_INTERRUPTED_AND_REAPED',flush=True)
print('B1_RUNNER_EXIT_CODE',exit_code,flush=True)
