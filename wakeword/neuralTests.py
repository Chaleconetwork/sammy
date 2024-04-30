import torch

array = [[2,3,4], [1,5,6]]
tensor1 = torch.tensor(array)
# print(tensor1)

device = (
    'cuda' if torch.cuda.is_available() else 'cpu'
)

print(f'Usando: {device}')