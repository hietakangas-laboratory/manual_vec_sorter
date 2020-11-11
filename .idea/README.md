# Manual_vec_sorter
## Author: Jack Morikka

This is a small program that takes tiffs with manual 'vectors' drawn in imageJ and saves all 
the vectors as vector.txt files and then moves them into the correct LAM files in a LAM analysis samples folder.
As in the IMARIS_to_LAM programme, this programme requires that your tiffs are named in 
the format: NAME_YYYY-MM-DD_XXXXXX. This is what the tiffs are usually called when they 
are derived from the AUROX microscope.

Instructions:

* Select the imageJ.exe file (usually somewhere like: "C:\hyapp\fiji-win64-1.52p\Fiji.app\ImageJ-win64.exe")
* Then select the input folder with the tiffs containing the manually drawn vectors (make sure that is all this folder contains).
* Finally select the LAM /analysis/samples folder with the samples corresponding to the tiffs. **N.B.** the sample folders must
have the same name as the tiffs e.g. 'OR_2020-08-31_145800' so that the programme can move the vector files to the correct folder.

