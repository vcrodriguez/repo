from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
im=fits.open("cumulo.fits")
im.info()
image=im[0].data
im.close()
#para ver el cumulo:
#plt.imshow(image,cmap='gray')
#plt.colorbar()
#plt.show()
#basic statistics
print('Min:', np.min(image))
print('Max:', np.max(image))
print('Mean:', np.mean(image))
print('Stdev:', np.std(image))
#plotting a histogram, me tira error :(
#print(type(image.flat))
#NBINS=50
#plt.hist(image.flat,NBINS)
#plt.show()
#grafico del cumulo
#plt.plot(np.arange(4000,4000+image[0].size), image[0],color="blue")
#plt.show()
