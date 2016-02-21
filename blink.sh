while [ true ]; do
	 sleep 6
	 python setimage.py imageinverted.pcx riboflav.in 26001
	 sleep 6
	 python setimage.py image.pcx riboflav.in 26001
done
