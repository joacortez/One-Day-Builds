from warnings import catch_warnings
import pikepdf
import sys


def deleteWatermark():
    inputFileName = input("Insert Path\n->").replace("\"", "")

    pdf = pikepdf.open(inputFileName, allow_overwriting_input=True)

    for page in pdf.pages:
        imageList = list(page.images.keys())
        # delete link
        try:
            del page["/Annots"][0]
        except:
            pass
        # delete image
        for image in imageList:
            del page["/Resources"]["/XObject"][image]

    pdf.save(inputFileName)
    print("File saved to {}".format(inputFileName))


if __name__ == "__main__":
    deleteWatermark()
