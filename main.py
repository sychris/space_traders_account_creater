import http.client
import auth_token as auth
import json

conn = http.client.HTTPSConnection("api.spacetraders.io")
ver = "/v2/"
auth_token = {"Authorization": "Bearer " + auth.token}


def main():
    user_name = "test"
    faction = "COSMIC"
    create_token(user_name, faction)


def create_token(my_user, my_faction):
    if auth.token != "":
        print("user already generated clear existing token to make anew!")
        exit()
    payload = "{\n  \"faction\": \"" + my_faction + "\",\n  \"symbol\": \"" + my_user + "\"}"
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json"
    }
    conn.request("POST", ver + "register", payload, headers)
    res = conn.getresponse()
    data = res.read()
    phased = json.loads(data)

    if "error" in phased:
        print("error" + str(phased["error"]))
    else:
        print("success")
        token = "token = \"" + phased["data"]["token"] + "\""
        print(phased["data"]["token"])
        file_path = "auth_token.py"
        with open(file_path, "w") as file:
            file.write(token)
        print(f"Token generated in {file_path}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
