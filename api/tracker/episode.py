class Episode(object):
  """
  Episode of a series.
  """
  def __init__(self, **kwargs):
    self.id = kwargs.get('id')
    self.name = kwargs.get('name')

  def __str__(self):
    return '{id}: {name}'.format(
      id=self.id,
      name=self.name
    )

