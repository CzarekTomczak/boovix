engine enum("imdb", "fdb", "filmweb")
title
description
rating
votes
poster_url
poster_blob # Is it performance wise to keep posters in database?
            # A better idea is to put them in directory with name
            # generated with md5(poster_url)
