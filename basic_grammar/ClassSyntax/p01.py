from abc import *

class Author(metaclass=ABCMeta):
    def __init__(self) -> bool:
        self.name = "송중기"
        self.age = 16

    @abstractclassmethod
    def readingScript(self, author):
        pass
        
class SongJunggi(Author):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
    
    def readingScript(self, author):
        print(f"태양의 후예를 촬영한 {author}가 대본을 읽습니다.")

if __name__ == '__main__':
    songJunggi = SongJunggi()
    songJunggi.readingScript("송중기")