class SocialNetwork:
    """
    This is the base class for social networks.
    """

    def __init__(self, name: str, users: int):
        self.name = name
        self.users = users

    def __str__(self) -> str:
        return f"{self.name} - {self.users} users"

    def __repr__(self) -> str:
        return f"SocialNetwork({self.name}, {self.users})"


class VK(SocialNetwork):

    def __init__(self, name: str, users: int, active_users: int):
        super().__init__(name, users)
        self.active_users = active_users

    def __str__(self) -> str:
        return f"{self.name} - {self.users} total users, {self.active_users} active users"

    def __repr__(self) -> str:
        return f"Vk ({self.name}, {self.users}, {self.active_users})"

    @staticmethod
    def promote_post(post: str) -> str:

        return f"Пост '{post}' был выложен."


if __name__ == "__main__":
    vk = VK("VK", 3000000, 1500000)
    print(vk)