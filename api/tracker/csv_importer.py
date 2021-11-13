import csv

from .episode import Episode

def parse_csv(filename, has_header=False):
  """
  Utility for parsing the episode ids and names
  into Python objects.

  Note: This is largely untested and should be
  used with caution.
  """
  with open(filename) as csvfile:
    reader = csv.reader(csvfile)

    header = []
    episodes = []
    for row in reader:
      if has_header:
        has_header = False
        header = row
        continue

      new_ep = Episode(
        id=row[0],
        name=row[1],
        viewed=False
      )
      episodes.append(new_ep)

  return episodes

