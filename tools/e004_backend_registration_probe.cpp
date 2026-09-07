#include "llama.h"
#include "ggml-backend.h"

#include <cstdio>

int main(int argc, char ** argv) {
    if (argc != 2) {
        std::fprintf(stderr, "usage: e004_backend_registration_probe <verified-runtime-libdir>\n");
        return 64;
    }

    llama_backend_init();
    ggml_backend_load_all_from_path(argv[1]);

    const size_t backend_count = ggml_backend_reg_count();
    std::printf("BACKEND_REGISTRY_COUNT=%zu\n", backend_count);
    std::printf("MODEL_BYTES_ACQUIRED=NO\n");
    std::printf("MODEL_LOAD_PERFORMED=NO\n");

    llama_backend_free();

    if (backend_count == 0) {
        std::fprintf(stderr, "BACKEND_REGISTRATION=INCOMPLETE_BACKEND_REGISTRATION_NOT_READY\n");
        return 78;
    }

    std::printf("BACKEND_REGISTRATION=PASS\n");
    return 0;
}
