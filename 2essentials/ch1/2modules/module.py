print("I am a module")
print(__name__)


if __name__ == "__main__":
    print(f"Module is executed direclty, so __name__ is {__name__}")
else:
    print(f"Module is import somwhere, so __name__ is {__name__}")