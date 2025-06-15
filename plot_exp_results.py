import matplotlib.pyplot as plt

vocab_sizes = [50, 100, 1000, 10000]

# Multi-class
multi_acc = [0.56225, 0.6165, 0.67225, 0.692]
multi_recall = [0.3100, 0.3739, 0.4596, 0.4670]
multi_f1 = [0.3996, 0.4655, 0.5460, 0.5576]

# Two-class
two_acc = [0.7285, 0.7840, 0.8410, 0.8735]
two_recall = [0.7285, 0.7841, 0.8412, 0.8736]
two_f1 = [0.7285, 0.7841, 0.8411, 0.8735]

plt.figure(figsize=(10, 5))

"""
# Multi-class plot
plt.subplot(1, 2, 1)
plt.plot(vocab_sizes, multi_acc, label='Accuracy')
plt.plot(vocab_sizes, multi_recall, label='Recall')
plt.plot(vocab_sizes, multi_f1, label='F1')
plt.title('Multi Class Naive Bayes')
plt.xlabel('Vocabulary Size')
plt.ylabel('Score')
plt.legend()
"""

# Two-class plot
plt.subplot(1, 2, 2)
plt.plot(vocab_sizes, two_acc, label='Accuracy')
plt.plot(vocab_sizes, two_recall, label='Recall')
plt.plot(vocab_sizes, two_f1, label='F1')
plt.title('2 Class Naive Bayes')
plt.xlabel('Vocabulary Size')
plt.ylabel('Score')
plt.legend()
plt.tight_layout()



plt.show()