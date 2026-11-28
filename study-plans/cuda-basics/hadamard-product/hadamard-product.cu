#include <cuda_runtime.h>

__global__ void hadamard_kernel(const float* A, const float* B, float* C, int M, int N) {
    // Write code here
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    int j = blockIdx.y * blockDim.y + threadIdx.y;
    if ((i < M) && (j < N)){
        C[i * N + j] = A[i * N + j] * B[i * N +j];
    }
    
}

extern "C" void solve(const float* A, const float* B, float* C, int M, int N) {
    dim3 threads(16, 16);
    dim3 blocks((M + 15) / 16, (N + 15) / 16);
    hadamard_kernel<<<blocks, threads>>>(A, B, C, M, N);
    cudaDeviceSynchronize();
}
