# AI Learning Notes

我的个人学习代码与面试复盘，记录算法、PyTorch 基础模块，以及 AI for Healthcare 中的图像和表格数据处理实践。

## 目录

```text
interview_code/
├── README.md                    # 面试问题、复杂度与实现细节
├── bubble_sort.py               # 冒泡排序
└── multihead_attention.py       # PyTorch 多头自注意力

ai_for_health/
├── README.md                    # 分类说明、依赖与使用注意点
├── image_processing/
│   └── preprocessing.py        # DICOM 转 NIfTI、重采样、非零区域裁剪
├── image_analysis/
│   └── extract_radiomics.py     # PyRadiomics 特征提取与导出
├── datasets/
│   └── medmnist_loader.py       # 医学图像数据集加载片段
└── tabular_learning/
    └── lightgbm_excel.py        # Excel 表格数据的分类示例
```

- [面试代码与复盘](interview_code/README.md)：冒泡排序和多头注意力的时间/空间复杂度、张量形状及常见追问。
- [AI for Healthcare 学习代码](ai_for_health/README.md)：图像处理、影像组学、医学图像数据集与表格学习。

## 快速开始

冒泡排序只依赖 Python 标准库：

```bash
python interview_code/bubble_sort.py
# 输入：3,1,2
# 输出：1,2,3
```

多头注意力示例需要 PyTorch：

```bash
python interview_code/multihead_attention.py
# 输出：torch.Size([2, 10, 64])
```

医疗 AI 部分保留为学习片段，部分文件依赖外部参数、数据路径或导入；具体用途和需要补充的内容见对应 README。

## 关于数据分类

**MedMNIST 属于医学图像数据集，不是表格数据。** 本仓库的表格学习示例是 `lightgbm_excel.py`。影像组学会把图像转成数值特征表，但特征提取本身归在图像分析。

## 学习资料

- [MedMNIST 官方介绍](https://medmnist.com/)
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [PyTorch MultiheadAttention 文档](https://docs.pytorch.org/docs/stable/generated/torch.nn.MultiheadAttention.html)

持续补充学习实现和面试中遇到的问题。
