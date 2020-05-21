# digmypics-downloader
Python-based command line tool for downloading finished images from the DigMyPics image digitization service

Once your order is paid for, you can use this program (along with your DigMyPics order number and your zip code) to download your images from DigMyPics.

I wrote this because the GUI-based downloader that DigMyPics provides does not restart automatically if the network connection goes down. Furthermore, when it is restarted manually, it seems to restart at the beginning.

This program does not restart automatically either, however when restarted, it picks up from where it left off.

Usage message:

```
usage: digmypics-downloader.py <ORDER-NUMBER> <ZIP-CODE> <LOCAL-DOWNLOAD-DIRECTORY>

       The program downloads all files for the given order number into the given download directory.
       If the photo exists already in the download directory, it does not try to download it.

```

Example run:

```
$ python digmypics-downloader.py 890000 03000 ~/Pictures/digmypics2
2099 photos in the order, 2022 left to go.
downloading /Users/ericwoudenberg/Pictures/digmypics2/Negatives_03/Negatives_03_006.jpg --  2.92s  3.67%  eta: 2020-05-21 09:58
downloading /Users/ericwoudenberg/Pictures/digmypics2/Negatives_03/Negatives_03_007.jpg --  2.82s  3.72%  eta: 2020-05-21 09:56
downloading /Users/ericwoudenberg/Pictures/digmypics2/Negatives_03/Negatives_03_008.jpg --  3.02s  3.76%  eta: 2020-05-21 09:58
downloading /Users/ericwoudenberg/Pictures/digmypics2/Negatives_03/Negatives_03_009.jpg --  2.74s  3.81%  eta: 2020-05-21 09:57
downloading /Users/ericwoudenberg/Pictures/digmypics2/Negatives_03/Negatives_03_010.jpg --  2.85s  3.86%  eta: 2020-05-21 09:57
downloading /Users/ericwoudenberg/Pictures/digmypics2/Negatives_03/Negatives_03_012.jpg --  2.94s  3.91%  eta: 2020-05-21 09:57
downloading /Users/ericwoudenberg/Pictures/digmypics2/Negatives_03/Negatives_03_013.jpg --  2.82s  3.95%  eta: 2020-05-21 09:57
downloading /Users/ericwoudenberg/Pictures/digmypics2/Negatives_03/Negatives_03_014.jpg --  3.54s  4.00%  eta: 2020-05-21 09:59
```

