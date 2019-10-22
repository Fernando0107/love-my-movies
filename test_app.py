from var import test

test = True

def test_brain(test):
  assert test == True


if __name__ == "__main__":
    test_brain(test)
    print("Everything passed")
