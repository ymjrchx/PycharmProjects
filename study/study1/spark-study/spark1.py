import findspark
findspark.init()

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession






# import findspark
# findspark.init()

def run():
    conf = SparkConf().setMaster("local").setAppName("11")
    context = SparkContext(conf=conf)

    textFile = context.textFile("file:///E:\\Program\\PycharmProjects\\study\\pyspark\\people.txt")
    print(textFile.count())


def run1():
    spark = SparkSession.builder.master("local").appName("spark-python").getOrCreate()



    df = spark.createDataFrame(
        [
            ['zhang3', 18, 65.5, '高中'],
            ['li4', 19, 50.2, '本科'],
            ['wang5', 20, 61.2, '本科'],
            ['zhao6', 21, 50.8, '本科'],
            ['zheng7', 22, 77.2, '硕士'],
            ['zhou8', 22, 80.7, '硕士'],
        ], schema=['姓名', '年龄', '体重', '学历']
    )
    # 制造几个空值
    df2 = spark.createDataFrame(
        [
            ['zhang3', 18, 65.5, '高中'],
            ['li4', 19, 50.3, '本科'],
            ['wang5', 20, None, '本科'],
            ['zhao6', 21, None, None],
            ['zheng7', 22, 77.2, None],
            ['zhou8', 22, 80.7, '硕士'],
        ], schema=['姓名', '年龄', '体重', '学历']
    )
    # 把姓名改成age，下面会用到
    df3 = spark.createDataFrame(
        [
            ['zhang3', 18, 65.5, '高中'],
            ['li4', 19, 50.2, '本科'],
            ['wang5', 20, 61.2, '本科'],
            ['zhao6', 21, 50.8, '本科'],
            ['zheng7', 22, 77.2, '硕士'],
            ['zhou8', 22, 80.7, '硕士'],
        ], schema=['姓名', 'age', '体重', '学历']
    )
    # 设置重复值
    df4 = spark.createDataFrame(
        [
            ['zhang3', 18, 65.5, '高中'],
            ['li4', 19, 50.2, '本科'],
            ['li4', 19, 50.2, '本科']
        ], schema=['姓名', 'age', '体重', '学历']
    )
    df.show()
    df2.show()
    df3.show()
    df4.show()

    # 缺失值填充
    df2.na.fill({'体重': 50.2, '学历': '本科'}).show()

    # 1.查看字段类型
    df.dtypes

    # 2.查看列名
    df.columns, len(df.columns)

    # 3.查看行数
    df.count()

    # 4.重命名列名
    df.withColumnRenamed('姓名', 'name')
    df.printSchema()

    # 选择列（select）
    df.select('年龄')  # 单列
    df.select('年龄', '学历')  # 两列
    df.select(df.年龄, df.学历)  # 两列

    # 选择行（filter或where）
    df.filter(df.年龄 > 19)
    df.where(df.年龄.between(19, 21))  # 闭区间

    # 选择列+行
    df.select('年龄', '学历').where(df.年龄.between(19, 21))  # 闭区间

    df.show()

    # 以上的方式，也可以用sql来选择
    df3.registerTempTable('person')
    spark.sql('select age,"学历" from person where "年龄">19')  # 英文不需要加双引号




if __name__ == '__main__':
    run()
