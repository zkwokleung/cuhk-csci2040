from os import error
import pickle as pk


def load_data(file):
    try:
        with open(file, 'rb') as f:
            result = pk.load(f)
    except error:
        print(error)
        print("ERROR: Target file does NOT exist!")
        result = {}

    return result


def most_follower(dictionary):
    result = [k for (k, v) in dictionary.items() if len(v) > 99]
    return result


def update():
    # Load data
    follower_data = load_data("followers.pydata")
    # Add follower
    follower_data["William Smith"] += ["Lorna Carrico"]
    # Add new user
    follower_data["Anne Smelcer"] = [
        "Christine Phillips", "Charles Mason", "Daisy Middleton"]
    # Remove user
    for v in follower_data.values():
        if "Mildred Jones" in v:
            v.remove("Mildred Jones")
    del follower_data["Mildred Jones"]
    # Save to file
    try:
        with open("followers-updated.pydata", 'wb') as f:
            pk.dump(follower_data, f)
    except:
        pass


def get_num_of_followers():
    follower_data = load_data("followers-updated.pydata")
    result = {k: len([i for i in v if len(follower_data[i]) >= 2])
              for (k, v) in follower_data.items()}
    return result


if __name__ == '__main__':
    # print({most_follower(load_data("followers-updated.pydata"))})
    update()
    print(get_num_of_followers())
    pass
