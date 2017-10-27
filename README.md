# ConvertLinuxKernelConfig2SourceInsightConditionsXml
A tool to convert linux kernel .config file to source insight's conditional source parsing xml config file.

## Usage ##
    usage: lkc2sicx.py [-h] [-s SRC_PATH] -d DEST_PATH
 
    optional arguments:
      -h, --help            show this help message and exit
      -s SRC_PATH, --src SRC_PATH
            linux kernel config file path, default: .config             
      -d DEST_PATH, --dest DEST_PATH
            source insight conditional parsing xml file path
