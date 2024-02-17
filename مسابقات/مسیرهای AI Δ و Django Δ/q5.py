class CinemaSystem:
    def __init__(self):
        self.movies = {}
        self.actors = {}
        self.movie_id_counter = 0
        self.actor_id_counter = 0

    def add_movie(self, title, date, quality):
        if len(title) > 20 or not (1888 <= int(date) <= 2024) or quality not in ["720p", "1080p", "4K"]:
            return self.error_message(title, date, quality)
        movie_id = self.movie_id_counter
        self.movies[movie_id] = {"title": title, "date": date, "quality": quality, "casts": []}
        self.movie_id_counter += 1
        return f"added successfully {movie_id}"

    def rem_movie(self, movie_id):
        if movie_id in self.movies:
            del self.movies[movie_id]
            return f"removed successfully {movie_id}"
        else:
            return "invalid movie id"

    def add_cast(self, name):
        if len(name) > 20 or not name.replace(" ", "").isalpha():
            return "invalid name"
        actor_id = self.actor_id_counter
        self.actors[actor_id] = {"name": name, "movies": []}
        self.actor_id_counter += 1
        return f"added successfully {actor_id}"

    def rem_cast(self, cast_id):
        if cast_id in self.actors:
            del self.actors[cast_id]
            for movie in self.movies.values():
                if cast_id in movie['casts']:
                    movie['casts'].remove(cast_id)
            return f"removed successfully {cast_id}"
        else:
            return "invalid cast id"

    def link_cast_to_movie(self, cast_id, movie_id):
        if cast_id not in self.actors or movie_id not in self.movies:
            return self.link_error_message(cast_id, movie_id)
        if cast_id in self.movies[movie_id]["casts"]:
            return "already linked"
        self.movies[movie_id]["casts"].append(cast_id)
        self.actors[cast_id]["movies"].append(movie_id)
        return f"successfully linked {cast_id} to {movie_id}"

    def show_movie(self, movie_id):
        if movie_id not in self.movies:
            return "invalid movie id"
        movie = self.movies[movie_id]
        casts = sorted(movie["casts"])
        return f'{{title:"{movie["title"]}", date:"{movie["date"]}", quality:"{movie["quality"]}", casts:{casts}}}'

    def show_cast(self, cast_id):
        if cast_id not in self.actors:
            return "invalid cast id"
        actor = self.actors[cast_id]
        movies = sorted(actor["movies"]) 
        return f'{{name:"{actor["name"]}", movies:{movies}}}'

    def error_message(self, title, date, quality):
        if len(title) > 20:
            return "invalid title"
        if not (1888 <= int(date) <= 2024):
            return "invalid date"
        if quality not in ["720p", "1080p", "4K"]:
            return "invalid quality"
        return ""

    def link_error_message(self, cast_id, movie_id):
        if cast_id not in self.actors:
            return "invalid cast id"
        if movie_id not in self.movies:
            return "invalid movie id"
        return ""
    
    def filter_movies_by_title(self, pattern):
        filtered_movie_ids = [movie_id for movie_id, movie in self.movies.items() if movie["title"].startswith(pattern)]
        return sorted(filtered_movie_ids)

    def filter_movies_by_date(self, operator, year):
        year = int(year)
        # Initialize an empty list to store filtered movie IDs
        filtered_movie_ids = []
        for movie_id, movie in self.movies.items():
            movie_year = int(movie["date"])  # Ensure the movie's date is an integer for comparison
            if operator == ">" and movie_year > year:
                filtered_movie_ids.append(movie_id)
            elif operator == "<" and movie_year < year:
                filtered_movie_ids.append(movie_id)
            elif operator == "=" and movie_year == year:
                filtered_movie_ids.append(movie_id)
            elif operator == ">=" and movie_year >= year:
                filtered_movie_ids.append(movie_id)
            elif operator == "<=" and movie_year <= year:
                filtered_movie_ids.append(movie_id)
        return sorted(filtered_movie_ids)

    def filter_movies_by_quality(self, quality):
        filtered_movie_ids = [movie_id for movie_id, movie in self.movies.items() if movie["quality"] == quality]
        return sorted(filtered_movie_ids)
    
    def execute_command(self, command):
        parts = command.split()
        action = parts[0]
        args = parts[1:]

        if action == "ADD-MOVIE":
            title, date, quality = args
            print(self.add_movie(title, date, quality))
        elif action == "REM-MOVIE":
            movie_id = int(args[0])
            print(self.rem_movie(movie_id))
        elif action == "ADD-CAST":
            name = " ".join(args)
            print(self.add_cast(name))
        elif action == "REM-CAST":
            cast_id = int(args[0])
            print(self.rem_cast(cast_id))
        elif action == "LINK-CAST-TO-MOVIE":
            cast_id, movie_id = map(int, args)
            print(self.link_cast_to_movie(cast_id, movie_id))
        elif action == "SHOW-MOVIE":
            movie_id = int(args[0])
            print(self.show_movie(movie_id))
        elif action == "SHOW-CAST":
            cast_id = int(args[0])
            print(self.show_cast(cast_id))
        if action.startswith("FILTER"):
            if action == "FILTER-MOVIES-BY-TITLE":
                pattern = args[0]
                result = self.filter_movies_by_title(pattern)
            elif action == "FILTER-MOVIES-BY-DATE":
                operator, year = args[0], args[1]
                result = self.filter_movies_by_date(operator, year)
            elif action == "FILTER-MOVIES-BY-QUALITY":
                quality = args[0]
                result = self.filter_movies_by_quality(quality)
            print(result)
        else:
            print(f"Unknown command: {action}")


system = CinemaSystem()
for _ in range(int(input())):
    command = input()
    system.execute_command(command)