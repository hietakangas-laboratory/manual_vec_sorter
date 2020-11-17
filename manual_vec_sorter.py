'''
Author: Jack Morikka.
A programme to save vector.txt files from tiffs with imageJ vector selection
and then to place these in the corresponding output directories with the same
name as the vector.txt file (but without the _Vector suffix)'''

import os
import logging
import shutil
from ij import IJ


def main(tiff_dir, analysis_dir):
    logging.basicConfig(
        filename='%s/manual_vector_sorter.log' % tiff_dir,
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%d-%m-%Y %H:%M:%S')

    logging.info('Starting vector sorter')
    py_file_loc = os.path.realpath(__file__)
    mvs_path = os.path.dirname(os.path.abspath(py_file_loc))
    runmacros(tiff_dir, mvs_path)
    movevectorfiles(tiff_dir, analysis_dir)
    logging.info("Process finished")

def runmacros(tiff_dir, mvs_path):

    for root, dirs, files in os.walk(tiff_dir):
        for file in files:
            if file.endswith(".tiff") or file.endswith(".tif"):
                try:
                    logging.info('.tiff file discovered: %s' % file)
                    tiff_path = os.path.join(root, file)
                    IJ.runMacroFile(mvs_path + r"\vector_saver.ijm", tiff_path)
                    IJ.run("Close All")
                except Exception as e:
                    logging.exception(str(e))

    logging.info("Vector.txt files created")


def movevectorfiles(tiff_dir, analysis_dir):

    vector_paths = []

    for root, dirs, files in os.walk(tiff_dir):
        for file in files:
            if file.endswith("Vector.txt"):
                logging.info("Vector.txt file discovered: %s" % file)
                vector_path = os.path.join(root, file)
                vector_paths.append(vector_path)

    logging.info(vector_paths)
    dirpaths = []


    for root, dirs, files in os.walk(analysis_dir):
        for dir in dirs:
            dirpath = os.path.join(root, dir)
            logging.info("Sample analysis directory found: %s"% dirpath)
            dirpaths.append(dirpath)

    logging.info(dirpaths)

    logging.info("Attempting to copy Vector.txt files to Sample analysis files")

    for vpath in vector_paths:
        for dirpath in dirpaths:
            if (os.path.basename(dirpath)).lower() in (os.path.basename(vpath)).lower():
                logging.info((os.path.basename(vpath)).lower())
                logging.info((os.path.basename(dirpath)).lower())
                try:
                    logging.info("Associated directory for %s found: %s" % (vpath, dirpath))
                    final_dest = os.path.join(dirpath, os.path.basename(vpath))
                    logging.info("Copying %s to %s" % (vpath, final_dest))
                    shutil.move(vpath, final_dest)
                    vec_rnme = dirpath+"\Vector.txt"
                    logging.info(vec_rnme)
                    vec_csv = dirpath+"\Vector.csv"
                    logging.info(vec_csv)
                    logging.info("Removing old Vector.csv or Vector.txt files")
                    if os.path.exists(vec_rnme):
                        os.remove(vec_rnme)
                    if os.path.exists(vec_csv):
                        os.remove(vec_csv)
                    logging.info("Renaming %s to %s" % (final_dest, vec_rnme))
                    os.rename(final_dest, vec_rnme)
                except Exception as e:
                    logging.exception(str(e))

    logging.info("Vector files moved")

#@String tiff_dir
#@String analysis_dir


main(tiff_dir, analysis_dir)

