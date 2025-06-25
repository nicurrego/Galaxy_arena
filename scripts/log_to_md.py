from utils.logger import promote_csv_to_md

def main():
    csv_path = "logs/experiment_results.csv"
    md_path = "logs/exp_records.md"
    notes = input("Enter notes for promotion: ")
    promote_csv_to_md(csv_path, md_path, row_idx=-1, extra_notes=notes)
    print("Promotion logged in Markdown.")

if __name__ == "__main__":
    main()