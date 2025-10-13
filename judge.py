import csv
import os
import sys

INPUT_DIR = "output_tweets_to_correct"          # dossier des CSV à juger
OUTPUT_DIR = "tweets_judged"  # dossier où stocker les CSV jugés

def judge_csv(file_path):
    print(f"\n🟢 Évaluation du fichier : {file_path}")
    judged_rows = []

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = ["tweet", "politiquement_correct"]

        for row in reader:
            # Trouve la colonne du tweet
            tweet = row.get("tweet") or row.get("text") or list(row.values())[0]

            print("\n🔹 Tweet :")
            print(tweet)
            try:
                note = input("👉 Note (1=très incorrect, 5=très correct) : ").strip()
                if note.lower() in ("exit", "quit"):
                    raise EOFError
                if not note.isdigit() or not (1 <= int(note) <= 5):
                    print("⚠️ Entrez un nombre entre 1 et 5.")
                    continue
                judged_rows.append({"tweet": tweet, "politiquement_correct": int(note)})
            except EOFError:
                print("\n🛑 Fin du script (CTRL+D détecté).")
                save_and_exit(file_path, judged_rows, fieldnames)
                sys.exit(0)

    save_and_exit(file_path, judged_rows, fieldnames)

def save_and_exit(file_path, judged_rows, fieldnames):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_path = os.path.join(OUTPUT_DIR, os.path.basename(file_path))

    with open(out_path, "w", newline="", encoding="utf-8") as out_f:
        writer = csv.DictWriter(out_f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(judged_rows)

    print(f"✅ Fichier noté sauvegardé dans : {out_path}")

    # Supprimer le fichier original
    os.remove(file_path)
    print(f"🗑️ Fichier original supprimé : {file_path}\n")

def main():
    print("=== Lancement du jugement des tweets ===")
    os.makedirs(INPUT_DIR, exist_ok=True)
    csv_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".csv")]

    if not csv_files:
        print("❌ Aucun fichier CSV trouvé dans le dossier 'output/'.")
        return

    for csv_file in csv_files:
        judge_csv(os.path.join(INPUT_DIR, csv_file))

    print("✅ Tous les fichiers ont été traités !")

if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print("\n🛑 Fin du script (CTRL+D).")
        sys.exit(0)
