import argparse
import pandas as pd
import os.path
import inspector

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="snpEff inspection tool")
    parser.add_argument("--target", required=False, help="snpEff TSV file")
    parser.add_argument("--disorder", required=False, help="Name genetic disorder", default="AGA")

    args = parser.parse_args()

    try:
        df = pd.read_hdf("./temp.h5", "snpEff")
    except:
        target_tsv_path = args.target
        if args.target == None:
            print("No cached data found. please specify tsv file with --target argument.")
            exit()
        if os.path.exists(args.target) == False:
            print("can't not find target file : ", args.target)
            exit()
        
        src_filename =  target_tsv_path 
        df = pd.read_csv(src_filename, "\t")
        df.to_hdf("./temp.h5", "snpEff")

    disorder_name = args.disorder
    if disorder_name == "AGA":
        inspector.check_AGA(df)
    else:
        print("Not supported")
        