#include "llama.h"
#include "ggml-backend.h"

#include <cstdio>

int main(int argc, char ** argv) {
    if (argc != 3) {
        std::fprintf(stderr, "usage: e004_model_load_probe <model.gguf> <verified-runtime-libdir>\n");
        return 64;
    }

    llama_backend_init();
    ggml_backend_load_all_from_path(argv[2]);

    const size_t backend_count = ggml_backend_reg_count();
    if (backend_count == 0) {
        std::fprintf(stderr, "BACKEND_REGISTRATION=INCOMPLETE_BACKEND_REGISTRATION_NOT_READY\n");
        std::fprintf(stderr, "BACKEND_REGISTRY_COUNT=0\n");
        llama_backend_free();
        return 78;
    }

    std::printf("BACKEND_REGISTRATION=PASS\n");
    std::printf("BACKEND_REGISTRY_COUNT=%zu\n", backend_count);

    llama_model_params params = llama_model_default_params();
    params.n_gpu_layers = 0;
    params.split_mode = LLAMA_SPLIT_MODE_NONE;

    std::printf("MODEL_LOAD_REACHED=YES\n");
    std::fflush(stdout);
    llama_model * model = llama_model_load_from_file(argv[1], params);
    if (model == nullptr) {
        std::fprintf(stderr, "EMPIRICAL_MODEL_LOAD_COMPATIBILITY=FAIL_MODEL_LOAD_ERROR\n");
        llama_backend_free();
        return 2;
    }

    std::printf("MODEL_OBJECT_CONSTRUCTION=PASS\n");
    std::printf("MODEL_FORWARD_PASS_PERFORMED=NO\n");
    std::printf("MODEL_INFERENCE_PERFORMED=NO\n");
    std::printf("GENERATION_PERFORMED=NO\n");
    std::printf("EMPIRICAL_MODEL_LOAD_COMPATIBILITY=PASS\n");

    llama_model_free(model);
    llama_backend_free();
    return 0;
}
