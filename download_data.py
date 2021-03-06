import wget

print('Downloading MNIST raw data...')
wget.download('http://www-users.math.umn.edu/~jwcalder/MNIST_raw.npz','./Data/MNIST_raw.npz')
print('Downloading MNIST vae data...')
wget.download('http://www-users.math.umn.edu/~jwcalder/MNIST_vae.npz','./Data/MNIST_vae.npz')
print('\n')

print('Downloading FashionMNIST raw data...')
wget.download('http://www-users.math.umn.edu/~jwcalder/FashionMNIST_raw.npz','./Data/FashionMNIST_raw.npz')
print('Downloading FashionMNIST vae data...')
wget.download('http://www-users.math.umn.edu/~jwcalder/FashionMNIST_vae.npz','./Data/FashionMNIST_vae.npz')
print('\n')

print('Downloading CIFAR raw data...')
wget.download('http://www-users.math.umn.edu/~jwcalder/cifar_raw.npz','./Data/cifar_raw.npz')
print('\n')

print('Downloading CIFAR aet data...')
wget.download('http://www-users.math.umn.edu/~jwcalder/cifar_aet.npz','./Data/cifar_raw.npz')
print('\n')
