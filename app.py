from flask import Flask, jsonify
import instaloader
import os

app = Flask(__name__)
L = instaloader.Instaloader()

@app.route("/instagram/<username>", methods=["GET"])
def get_instagram_profile(username):
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        data = {
            "name": profile.full_name,
            "username": profile.username,
            "bio": profile.biography,
            "profile_pic_url": profile.profile_pic_url,
            "followers": profile.followers,
            "following": profile.followees,
            "posts": profile.mediacount,
            "is_verified": profile.is_verified,
            "is_private": profile.is_private
        }
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
