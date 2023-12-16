import numpy as np
# 주어진 샘플 데이터
sample_data = np.array([1, 2, 3, 4, 5])
# 부트스트랩 샘플링
num_bootstrap_samples = 1000
bootstrap_samples = np.random.choice(sample_data,(num_bootstrap_samples, len(sample_data)), replace=True)
# 부트스트랩 평균 계산
bootstrap_means = np.mean(bootstrap_samples, axis=1)
# 95% 신뢰 구간 계산
confidence_interval = np.percentile(bootstrap_means, [2.5, 97.5])
print("95% 신뢰 구간:", confidence_interval)
