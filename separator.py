import csv
import os
import sys


def split_csv(file_path, lines_per_file=25, output_dir="output_tweets_to_correct"):
	# Vérification du fichier
	if not os.path.exists(file_path):
		print(f"Fichier introuvable : {file_path}")
		return

	# Création du dossier de sortie
	os.makedirs(output_dir, exist_ok=True)

	with open(file_path, "r", newline="", encoding="utf-8") as csvfile:
		reader = list(csv.reader(csvfile))
		header = reader[0]
		data = reader[1:]

		total_lines = len(data)
		num_files = (total_lines + lines_per_file - 1) // lines_per_file

		for i in range(num_files):
			start = i * lines_per_file
			end = start + lines_per_file
			chunk = data[start:end]

			output_filename = os.path.join(
				output_dir,
				f"{os.path.splitext(os.path.basename(file_path))[0]}_{i + 1}.csv"
			)

			with open(output_filename, "w", newline="", encoding="utf-8") as outfile:
				writer = csv.writer(outfile)
				writer.writerow(header)
				writer.writerows(chunk)

			print(f"Fichier créé : {output_filename} ({len(chunk)} lignes)")


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("❗ Utilisation : python split_csv.py <fichier.csv> [nombre_de_lignes]")
		sys.exit(1)

	file_path = sys.argv[1]
	lines_per_file = int(sys.argv[2]) if len(sys.argv) > 2 else 25

	split_csv(file_path, lines_per_file)
