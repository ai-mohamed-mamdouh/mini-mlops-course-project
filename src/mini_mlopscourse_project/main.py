from mini_mlopscourse_project.models import ModelFactory

iris_model = ModelFactory.create('iris')

if __name__ == '__main__' :
    print('===============================')
    print(iris_model)
    print('===============================')