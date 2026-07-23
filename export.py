import csv
def export_csv(rows,path):
    with open(path,"w",newline="") as f:
        w=csv.writer(f);w.writerows(rows)
