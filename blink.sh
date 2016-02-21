while [ true ]; do
	 sleep 6
	 python rawimage.py imageinverted.pcx riboflav.in 26001
	 sleep 6
	 python rawimage.py image.pcx riboflav.in 26001
done
