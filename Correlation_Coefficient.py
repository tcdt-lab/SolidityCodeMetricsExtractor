import numpy as np
from scipy.stats import pearsonr, spearmanr, kendalltau


class CorrelationCoefficient(object):

    def __init__(self, file_name):
         self.file_name = file_name

    def sloc_mccabe(self):

        data = np.genfromtxt(self.file_name, delimiter=',')
        x = data[:, 0]
        y = data[:, 1]

        # Pearson correlation coefficient
        pearson_corr, _ = pearsonr(x, y)

        # Spearman correlation coefficient
        spearman_corr, _ = spearmanr(x, y)

        # Kendall correlation coefficient
        kendall_corr, _ = kendalltau(x, y)

        print('SLOC and McCabe:')
        print("Pearson correlation coefficient:", pearson_corr)
        print("Spearman correlation coefficient:", spearman_corr)
        print("Kendall correlation coefficient:", kendall_corr)
        print('///////////////////////////////////////////////////////////////////////////////////////')


    def sloc_hv(self):
        data = np.genfromtxt(self.file_name, delimiter=',')
        x = data[:, 0]
        y = data[:, 2]

        # Pearson correlation coefficient
        pearson_corr, _ = pearsonr(x, y)

        # Spearman correlation coefficient
        spearman_corr, _ = spearmanr(x, y)

        # Kendall correlation coefficient
        kendall_corr, _ = kendalltau(x, y)

        print('SLOC and Halstead Volume')
        print("Pearson correlation coefficient:", pearson_corr)
        print("Spearman correlation coefficient:", spearman_corr)
        print("Kendall correlation coefficient:", kendall_corr)

        print('///////////////////////////////////////////////////////////////////////////////////////')


    def sloc_mi(self):
        data = np.genfromtxt(self.file_name, delimiter=',')
        x = data[:, 0]
        y = data[:, 3]

        # Pearson correlation coefficient
        pearson_corr, _ = pearsonr(x, y)

        # Spearman correlation coefficient
        spearman_corr, _ = spearmanr(x, y)

        # Kendall correlation coefficient
        kendall_corr, _ = kendalltau(x, y)

        print('SLOC and Maintainability Index')
        print("Pearson correlation coefficient:", pearson_corr)
        print("Spearman correlation coefficient:", spearman_corr)
        print("Kendall correlation coefficient:", kendall_corr)

        print('///////////////////////////////////////////////////////////////////////////////////////')


    def mccabe_hv(self):
        data = np.genfromtxt(self.file_name, delimiter=',')
        x = data[:, 1]
        y = data[:, 2]

        # Pearson correlation coefficient
        pearson_corr, _ = pearsonr(x, y)

        # Spearman correlation coefficient
        spearman_corr, _ = spearmanr(x, y)

        # Kendall correlation coefficient
        kendall_corr, _ = kendalltau(x, y)

        print('McCabe and Halstead volume')
        print("Pearson correlation coefficient:", pearson_corr)
        print("Spearman correlation coefficient:", spearman_corr)
        print("Kendall correlation coefficient:", kendall_corr)

        print('///////////////////////////////////////////////////////////////////////////////////////')


    def mccabe_mi(self):
        data = np.genfromtxt(self.file_name, delimiter=',')
        x = data[:, 1]
        y = data[:, 3]

        # Pearson correlation coefficient
        pearson_corr, _ = pearsonr(x, y)

        # Spearman correlation coefficient
        spearman_corr, _ = spearmanr(x, y)

        # Kendall correlation coefficient
        kendall_corr, _ = kendalltau(x, y)

        print('McCabe and Maintainability Index')
        print("Pearson correlation coefficient:", pearson_corr)
        print("Spearman correlation coefficient:", spearman_corr)
        print("Kendall correlation coefficient:", kendall_corr)

        print('///////////////////////////////////////////////////////////////////////////////////////')


    def hv_mi(self):
        data = np.genfromtxt(self.file_name, delimiter=',')
        x = data[:, 2]
        y = data[:, 3]


        # Pearson correlation coefficient
        pearson_corr, _ = pearsonr(x, y)

        # Spearman correlation coefficient
        spearman_corr, _ = spearmanr(x, y)

        # Kendall correlation coefficient
        kendall_corr, _ = kendalltau(x, y)

        print('Halstead volume and Maintainability Index')
        print("Pearson correlation coefficient:", pearson_corr)
        print("Spearman correlation coefficient:", spearman_corr)
        print("Kendall correlation coefficient:", kendall_corr)

        print('///////////////////////////////////////////////////////////////////////////////////////')


if __name__ == '__main__':
    file_name = 'results_method_level.csv'
    object_method_level = CorrelationCoefficient(file_name)
    print(object_method_level.sloc_mccabe())
    print(object_method_level.sloc_hv())
    print(object_method_level.sloc_mi())
    print(object_method_level.mccabe_hv())
    print(object_method_level.mccabe_mi())
    print(object_method_level.hv_mi())
    file_name = 'results_class_level.csv'
    object_method_level = CorrelationCoefficient(file_name)
    print(object_method_level.sloc_mccabe())
    print(object_method_level.sloc_hv())
    print(object_method_level.sloc_mi())
    print(object_method_level.mccabe_hv())
    print(object_method_level.mccabe_mi())
    print(object_method_level.hv_mi())
