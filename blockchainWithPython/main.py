import block
import blockchain


blockchain_instance = blockchain.Blockchain()

block_a = block.Block({"name": "john"})
block_b = block.Block({"name": "neu"})

blockchain_instance.addNewBlock(block_a)
blockchain_instance.addNewBlock(block_b)

blockchain_instance.checkValidity()

blockchain_instance.deleteBlock(1)

print()

blockchain_instance.checkValidity()
