def instaprofile(user):
    r = requests.get("http://apitrojans.herokuapp.com/instagram/user?username={}".format(str(user)))
    data=r.text
    data=json.loads(data)
    username = data["result"]["username"]
    name = data["result"]["fullname"]
    picture = data["result"]["profile_img"]
    biography = data["result"]["bio"]
    followers = data["result"]["followers"]
    following = data["result"]["following"]
    private = data["result"]["private"]
    media = data["result"]["media"]
    biography_link = data["result"]["external_url"]
    result = {
        "status":"200",
        "creator":"Asa Xyz",
        "result": {
            "username": username,
            "fullname": name,
            "profile_img": picture,
            "bio": biography,
            "bio_link":biography_link,
            "followers": followers,
            "following": following,
            "media": media,
            "private": private
        }
    }
    return(result)
