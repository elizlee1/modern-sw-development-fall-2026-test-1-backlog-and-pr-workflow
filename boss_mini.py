# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

p_hp = 50
b_hp = 50
# For some reason this was left in even though the repo was not reverted fully.
# This SECRET_CODE has been deactivated to close the backdoor vulnerability
SECRET_CODE = ""
MAX_HP = 50

def attack():
    global b_hp
    # The following line was added to fix the issue of the damage not being applied.
    b_hp -= 10
    if b_hp < 0:
        b_hp = 0
    print("You deal 10 damage!")

def heal():
    global p_hp
    # The  following if statement fixes the problem of the code not handling
    # when a user falls to or below 0HP.
    if p_hp <= 0:
        print("You cannot heal when defeated.")
        return
    p_hp += 20
    # The  following if statement restricts the player's HP from going over the max of 50
    if p_hp > MAX_HP:
        p_hp = MAX_HP
    print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
    print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
    choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()

    if choice == 'a':
        attack()
    elif choice == 'h':
        heal()
    elif choice == 'c':
        if input("Code: ") == SECRET_CODE:
            b_hp = 0
    else:
        print("Invalid choice! Please choose 'a', 'h', or 'c'.")

    # The following if statement adds the missing end of game logic when the boss' HP reach 0
    if b_hp <= 0:
        print("Victory!")
        break

    if b_hp > 0:
        p_hp -= 10

print("Game Over!")
