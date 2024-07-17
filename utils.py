import random

def get_random_phrase_from_file(file_path):
  try:
    with open(file_path, 'r', encoding='utf-8') as file:
      phrases = file.readlines()
    return random.choice(phrases).strip()
  except FileNotFoundError:
    return "Файл не найден."
  except Exception as e:
    return f"Произошла ошибка: {e}"

def generate_text(stats, account):
  kills, deaths, assists = stats["kills"],stats["deaths"],stats["assists"]
  name = account["profile"]["personaname"]
    
  if(is_win(stats)):
    phrase = get_random_phrase_from_file("assets/phrases_good.txt")
  else:
    phrase = get_random_phrase_from_file("assets/phrases_bad.txt")
  return f"[{name}] {phrase} - {kills}/{deaths}/{assists}"

def is_win(stats):
  is_radiant = stats["player_slot"] < 100
  is_radiant_win = stats["radiant_win"]
  return (is_radiant == is_radiant_win) or ((not is_radiant) == (not is_radiant_win))