import numpy as np
import distanz

class Operation:

    def __str__(self) -> str:
        return self.aktion + " " + self.transaktion + " " + self.element
    
    def __init__(self) -> None:
        self.aktion : str = None
        self.transaktion : str = None
        self.element : str = None


class Konflikten:
    def __init__(self) -> None:
        self.matrix = np.zeros((10,10))
        self.list = list()
        

    def print(self) -> str:
        for k in self.list:
            print(str(k[0]) + " -> " + str(k[1]))
        
        print("\n\n")
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if (self.matrix[i][j] == 1):
                    print(str(i) + " -> " + str(j))

    def add(self, t1,t2):
        self.list.append((t1, t2))

        t1 = int(t1.transaktion)
        t2 = int(t2.transaktion)

        self.matrix[t1][t2] = 1


class K_data:
    def __init__(self, data, k):
        self.data = data
        self.k = k
        self.centroids = []
        self.clusters = []
        self.distanz = []

        self.clusters_num = []

    def init_centroids(self):
        for i in range(self.k):
            self.centroids.append(self.data[i])

    # def init_clusters_num(self):
    #     self.clusters_num = []
    #     for i in range(self.k):
    #         self.clusters_num.append([])


    def init_clusters(self):
        self.clusters = []
        self.clusters_num = []
        for i in range(self.k):
            self.clusters.append([])
            self.clusters_num.append([])


    def init_distanz(self):
        self.distanz = []
        for i in range(self.k):
            self.distanz.append([])

    def calc_distanz(self, distanzfunktion):
        self.init_distanz()
        
        for i in range(self.k):
            for j in range(len(self.data)):
                self.distanz[i].append(distanzfunktion(self.centroids[i], self.data[j]))

    def calc_clusters(self):

        self.init_clusters()
        
        for i in range(len(self.data)):
            min = self.distanz[0][i]
            cluster = 0
            for j in range(self.k):
                if self.distanz[j][i] < min:
                    min = self.distanz[j][i]
                    cluster = j
            self.clusters[cluster].append(self.data[i])
            self.clusters_num[cluster].append(i + 1)

    def calc_new_centroids(self):
        for i in range(self.k):
            sum = [0, 0]
            for j in range(len(self.clusters[i])):
                sum[0] += self.clusters[i][j][0]
                sum[1] += self.clusters[i][j][1]
            self.centroids[i] = [sum[0] / len(self.clusters[i]), sum[1] / len(self.clusters[i])]

    # def calc_single_linkage(self, distanzfunktion):
    #     matrix = self.distanz_matrix(distanzfunktion)
    #     min = matrix[0][1]
    #     min_i = 0
    #     min_j = 1
    #     for i in range(len(matrix)):
    #         for j in range(len(matrix)):
    #             if matrix[i][j] < min:
    #                 min = matrix[i][j]
    #                 min_i = i
    #                 min_j = j

    #     print("Single linkage: " + str(min_i) + " " + str(min_j))

    def calc(self, iterations, distanzfunktion):
        # self.init_centroids()
        self.init_clusters()
        self.init_distanz()

        for i in range(iterations):
            print("Iteration " + str(i) + ":\n")
            self.calc_distanz(distanzfunktion)
            self.calc_clusters()
            self.calc_new_centroids()
            self.print()
            print("\n\n")



    def print(self):
        for i in range(self.k):
            print("Cluster " + str(i) + ": " + str(self.clusters[i]))
            print("Cluster num " + str(i) + ": " + str(self.clusters_num[i]))

        for i in range(self.k):
            print("Centroid " + str(i) + ": " + str(self.centroids[i]))





def distanz_matrix(data, distanzfunktion):
    matrix = np.zeros((len(data), len(data)))
    
    for i in range(len(data)):
        for j in range(len(data)):
            matrix[i][j] = distanzfunktion(data[i], data[j])
            # print(distanzfunktion(self.data[i], self.data[j]))

    return matrix

def parse_input():
    data = list()
    centroids = list()
    while(True):
        punkt = input("Punkte: ")
        if (punkt == ""):
            break

        punkt = punkt.split(",")
        data.append((float(punkt[0]), float(punkt[1])))

    centroid  = "0"
    while(True):
        centroid = input("Centroid: ")
        if (centroid == "" or centroid == "0"):
            break


        centroid = centroid.split(",")
        centroids.append((float(centroid[0]), float(centroid[1])))

    k = int(input("Anzahl Cluster: "))

    instance =  K_data(data, k)

    if centroid == "0":
        instance.init_centroids()
    else:
         instance.centroids = centroids

    return instance

def run_kmeans():
    instance = parse_input()
    
    iterations = int(input("Anzahl Iterationen: "))
    instance.calc(iterations, distanz.euklidisch)
    instance.print()



def run_distance_matrix(func):
    # parse input 
    data = list()
    while(True):
        punkt = input("Punkte: ")
        if (punkt == ""):
            break

        punkt = punkt.split(",")
        data.append([float(x) for x in punkt])

    matrix  = distanz_matrix(data, func)
    print(str(matrix))

def run_calc(func):
    data = list()
    while(True):
        punkt = input("Punkte: ")
        if (punkt == ""):
            break

        punkt = punkt.split(",")
        data.append([float(x) for x in punkt])

    print(func(data[0], data[1]))


def linear_regression():
    data = list()
    while(True):
        punkt = input("Punkte: ")
        if (punkt == ""):
            break

        punkt = punkt.split(",")
        data.append([float(x) for x in punkt])

    print("Berechnung der Regressionsgeraden mit der Methode der kleinsten Quadrate")

    x = np.array([d[0] for d in data])
    y = np.array([d[1] for d in data])

    # number of points
    n = np.size(x)
  
    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)
  
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
  
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
  
    print("Estimated coefficients:\nb_0 = {}  \nb_1 = {}".format(b_0, b_1))


def konflikten():
    schedule = list()



    currOperation = Operation()

    while(True):
        char = input()

        match char:
            case "R"| "W" | "r" | "w":
                currOperation.aktion = char.lower()
            case "1" | "2" | "3"| "4" | "5" | "6" | "7" | "8" | "9" | "0":
                currOperation.transaktion = char
            case "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" :
                currOperation.element = char
            case ")":
                schedule.append(currOperation)
                currOperation = Operation()
            case "+":
                break
            case _ :
                pass

    konflikten = Konflikten()

    for i in range(len(schedule)):
        for j in range(i+1, len(schedule)):
            t1 = schedule[i]
            t2 = schedule[j]
            if (t1.element == t2.element):
                if (t1.aktion == "w" or t2.aktion == "w"):
                    if (t1.transaktion != t2.transaktion):
                        konflikten.add(t1, t2)

    print("Konflikten: \n\n\n")
    konflikten.print()

class Precision:
    def __init__(self):
        self.correct_positive = 0
        self.false_positive = 0

        self.correct_negative = 0
        self.false_negative = 0

    def add(self, actual, predicted):
        if (actual == 1):
            if (predicted == 1):
                self.correct_positive += 1
            else:
                self.false_negative += 1
        else:
            if (predicted == 1):
                self.false_positive += 1
            else:
                self.correct_negative += 1

    def accuracy(self):
        print(str( (self.correct_positive + self.correct_negative) / (self.correct_positive + self.correct_negative + self.false_positive + self.false_negative)))
    def precision(self):
        print(str( self.correct_positive / (self.correct_positive + self.false_positive)))
    def recall(self):
        print(str( self.correct_positive / (self.correct_positive + self.false_negative)))
    def f1_score(self):
        print(str( 2 * self.correct_positive / (2 * self.correct_positive + self.false_positive + self.false_negative)))


def run_precision():
    p = Precision()

    while(True):
        data = input("Actual, Predicted: ")
        if (data == ""):
            break
        data = data.split(",")
        p.add(int(data[0]), int(data[1]))

    while(True):
        data = input("1 -> Accuracy, 2 -> Precision, 3 -> Recall:, 4 -> F1-Score: ")
        if (data == ""):
            break
        elif (data == "1"):
            p.accuracy()
        elif (data == "2"):
            p.precision()
        elif (data == "3"):
            p.recall()
        elif (data == "4"):
            p.f1_score()




def main():
    match input("Clustering  funktion:\n1 -> kmeans\n2 -> matrix max\n3 -> matrix manhattan\n4 -> matrix euklidisch\n5 -> max\n6 -> manhattan\n7 -> euklidisch\n8 -> lineare regression\n9 -> Konflikte\n0 -> precision and stuff\n\t"):
        case "1": run_kmeans()
        case "2": run_distance_matrix(distanz.maxnorm)
        case "3": run_distance_matrix(distanz.manhattan)
        case "4": run_distance_matrix(distanz.euklidisch)
        case "5": run_calc(distanz.maxnorm)
        case "6": run_calc(distanz.manhattan)
        case "7": run_calc(distanz.euklidisch)
        case "8": linear_regression()
        case "9": konflikten()
        case "0": run_precision()

        case _ : print("Falsche Eingabe")

    input("Press Enter to continue...")
    print("\n\n\n\n")
    main()

main()
