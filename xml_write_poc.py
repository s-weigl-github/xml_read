###
###
###

from xml.etree.ElementTree import XMLParser

maxDepth = None

class MaxDepth:
  maxDepth = 0
  depth = 0
  def start(self, tag, attrib):
    self.depth +=1
    if self.depth > self.maxDepth:
      self.maxDepth = self.depth
  def end(self, tag):
    self.depth -=1
  def data(self, data):
    pass
  def close(self):
    return self.maxDepth

  target = MaxDepth()
  parser = XMLParser(target=target)
  exampleXml = """
    <a>
      <b>
      </b>
      <b>
        <c>
          <d>
          </d>
        </c>
      </b>
    </a> """

  parser.feed(exampleXml)
  parser.close()
