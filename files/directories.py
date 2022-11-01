def files_checker(file, directory):
    hash1 = hash_manager(file)
    zeros1 = zeros_counter(hash1)
    winner = file

    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if checker(file, path):
            hash2 = hash_manager(path)
            zeros2 = zeros_counter(hash2)

            if zeros2 > zeros1:
                winner = filename
    return winner