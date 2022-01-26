from block import Block


class Blockchain():

    def __init__(self):
        self.blockchain = [self.startChain()]

    def startChain(self):
        return Block({})

    def lastBlock(self):
        return self.blockchain[-1]

    def addNewBlock(self, newBlock):
        newBlock.previousHash = self.lastBlock().thisBlockHash
        newBlock.computeHash()
        self.blockchain.append(newBlock)

    # for debug

    def deleteBlock(self, index):
        del self.blockchain[index]

    def checkValidity(self):
        for index, block in enumerate(self.blockchain[1:], start=1):
            print(
                f'checking block               | {index}')
            print(
                f'checking block with previous | {index - 1}')

            if(block.thisBlockHash != block.checkHash() or
               block.previousHash != self.blockchain[index - 1].thisBlockHash):
                print('not valid')
            else:
                print('valid')
