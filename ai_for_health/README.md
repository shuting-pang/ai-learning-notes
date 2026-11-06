# AI for Healthcare 学习代码

按代码处理的对象分类：图像预处理、图像分析、医学图像数据集和表格学习。

| 分类 | 文件 | 实际内容 |
| --- | --- | --- |
| 图像预处理 | [preprocessing.py](image_processing/preprocessing.py) | SimpleITK 的 DICOM→NIfTI 转换、体素重采样，以及非零区域裁剪 |
| 图像分析 / 影像组学 | [extract_radiomics.py](image_analysis/extract_radiomics.py) | 从图像和 ROI 提取一阶、形状、LoG、Wavelet 等特征，并导出特征表 |
| 医学图像数据集 | [medmnist_loader.py](datasets/medmnist_loader.py) | 按 MedMNIST 子集加载图像并构建 DataLoader |
| 表格学习 | [lightgbm_excel.py](tabular_learning/lightgbm_excel.py) | 读取 Excel 表格、构造特征、训练 LightGBM 并导出预测 |

## MedMNIST 为什么不放在表格分类下？

[MedMNIST](https://medmnist.com/) 提供标准化的二维和三维医学图像及分类标签。`medmnist_loader.py` 通过 `INFO` 找到图像数据集类，再构建图像 DataLoader，因此归到 `datasets/`。NumPy 文件格式或附带标签，不会把图像数据本身变成表格数据。

影像组学是另一个概念：它从医学图像中提取数值特征，结果可以供表格模型使用，但这里的脚本负责的是图像特征提取，因此放在 `image_analysis/`。

## 使用说明

这些是保留的学习片段，并非统一封装的训练流水线。运行前需要对应数据、路径和依赖。

- **图像预处理**：需要 NumPy 和 SimpleITK；原片段未包含导入语句。图像与 ROI 使用的插值方式应区分，图像通常用线性插值，离散标签通常用最近邻插值。
- **影像组学**：需要 PyRadiomics、SimpleITK、NumPy、pandas、six、os 等导入及 Excel 写入依赖。原脚本包含按位置跳过 37 项、固定 1052 列的假设，使用不同配置时应根据实际特征名核对。
- **MedMNIST**：需要 `medmnist`、PyTorch，以及外部定义的 `args`、`data`、`train_transforms` 和 `test_transforms`。原变量 `test_dataset` 实际使用 `split='val'`，对应验证集，不是独立测试集。
- **Excel / LightGBM**：需要 pandas、NumPy、LightGBM 和 Excel 读取依赖，并配置输入路径与标签列。原代码对 object 列调用 `isnull()`，实际构造的是缺失指示变量，并非注释中所称的目标编码；训练和预测使用的列还需要按实际表头对齐。

目录整理保留了这四个医疗 AI 片段的原始代码内容，以便后续逐步补全和复盘。
