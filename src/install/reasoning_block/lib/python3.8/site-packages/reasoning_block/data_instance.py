from os import replace
import numpy as np
import pickle

class Dataset:
    def __init__(self,data_points=[],labels=[],prep_data=[],test_set=[],test_labels=[],test_prep=[]):
        self.dataset = [data_points,labels,prep_data]
        self.test_set = [test_set, test_labels,test_prep]

    def append_data(self,data_point, label, prep):
        '''Appends a data point, with the related label, to the dataset collection.

        Parameters:
            Array with the new data point and an object, representing the label

        Returns: 
            None.
        '''
        self.dataset[0].append(data_point)
        self.dataset[1].append(label)
        if prep != []:
            self.dataset[2].append(prep)
    
    def append_test(self,data_point, label, prep=[]):
        '''Appends a data point, with the related label, to the test set collection.

        Parameters:
            Array with the new data point and an object, representing the label

        Returns: 
            None.
        '''
        self.test_set[0].append(data_point)
        self.test_set[1].append(label)
        if prep != []:
            self.test_set[2].append(prep)

    def get_data(self):
        '''Gets the data points.

        Parameters:
            None.

        Returns: 
            List containing the data points.
        '''
        return self.dataset[0]

    def get_data_as_array(self):
        '''Gets the data points, in a shape of a NumPy array.

        Parameters:
            None.

        Returns: 
            NumPy array containing the data points.
        '''
        return np.array(self.dataset[0])
        
    def get_data_dim(self):
        '''Gets the dimensionality of a single data point.

        Parameters:
            None.

        Returns: 
            Tuple representing the dimensionality of a data point in the dataset.
        '''
        return self.get_data_as_array().shape[1:]

    def get_label(self):
        '''Gets the label of the first data point. Useful, if you are sure data have the same label.

        Parameters:
            None.

        Returns: 
            A list with the labels of the dataset.
        '''
        return self.dataset[1][0]

    def get_labels(self):
        '''Gets the labels of the dataset.

        Parameters:
            None.

        Returns: 
            A list with the labels of the dataset.
        '''
        return self.dataset[1]

    def get_labels_as_array(self):
        '''Gets the labels of the dataset, in a shape of a NumPy array, if applicable.

        Parameters:
            None.

        Returns: 
            NumPy array containing the labels of the dataset, if applicable.
        '''
        return np.array(self.dataset[1])
    
    def get_size(self):
        '''Gets the number of data points.

        Parameters:
            None.

        Returns: 
            Integer representing the number of data points in the dataset.
        '''
        return len(self.dataset[0])

    def get_test(self):
        '''Gets the test set of the dataset.

        Parameters:
            None.

        Returns: 
            List representing the test set of the dataset.
        '''
        return self.test_set[0]
    
    def get_test_as_array(self):
        '''Gets the test set of the dataset, in the shape of a NumPy array.

        Parameters:
            None.

        Returns: 
            NumPy array containing the test set of the dataset.
        '''
        return np.array(self.test_set[0])

    def get_test_dim(self):
        '''Gets the dimensionality of a single data point.

        Parameters:
            None.

        Returns: 
            Tuple representing the dimensionality of a data point in the dataset.
        '''
        return self.get_data_as_array().shape[1:]

    
    def get_test_labels(self):
        '''Gets the labels of the test set of the dataset.

        Parameters:
            None.

        Returns: 
            Tuple representing the dimensionality of a data point in the dataset.
        '''
        return self.test_set[1]

    def get_test_labels_as_array(self):
        '''Gets the labels of the test set, in a shape of a NumPy array, if applicable.

        Parameters:
            None.

        Returns: 
            NumPy array containing the labels of the test set of the dataset, if applicable.
        '''
        return np.array(self.test_set[1])

    def get_test_size(self):
        '''Gets the number of instances of the training set.

        Parameters:
            None.

        Returns: 
            Integer representing the number of data points in the dataset.
        '''
        return len(self.test_set[0])

    def load(self, file_name=''):
        '''Loads a Dataset object and uses it to initialise the original one. It will be loaded the same path of where this method is called.
        If the dataset is not empty, it will invoke the sum(new_dataset) method.

        Parameters:
            Name of the file to load, that must include '.pickle' at the end

        Returns:
            None.
        
        '''
        
        dataset = pickle.load(open(file_name, 'rb'))
        dataset = dataset[0]
        
        if dataset.get_size()==0: #Assumption of never having just a test set to load
            dummy = self.unite(dataset)
            self.dataset = [dummy.get_data(),dummy.get_labels()]
            self.test_set = [dummy.get_test(), dummy.get_test_labels()]            
        else:
            for i in range(dataset.get_size()):
                self.dataset[0].append(dataset.dataset[0][i])
                self.dataset[1].append(dataset.dataset[1][i])
                if dataset.dataset[2] != []:
                    self.dataset[2].append(dataset.dataset[2][i])
            for i in range(dataset.get_test_size()):
                self.test_set[0].append(dataset.test_set[0][i])
                self.test_set[1].append(dataset.test_set[1][i])
                if dataset.test_set[2] != []:
                    self.test_set[2].append(dataset.test_set[2][i])
    
    def make_test_set(self, test_set_size):
        '''Generates a test set that will be stored in the variable itself. Good performances are granted if you call the function while 
        the dataset is still composed by instances with the same label. If there is more than one label in the dataset, it still can be used, but 
        it won't guarantee balance of instances in the test set.

        Parameters:
            Integer representing the desired size of the test set.

        Returns:
            None.
        '''
        sampled = np.random.choice(len(self.dataset[0]),test_set_size, replace = False)
        #disp = itertools.permutations(indexes, test_set_size)
        #deh=list(disp)
        #d=list(deh[0])

        for i in sampled:
            self.test_set[0].append(self.dataset[0][i])
            self.test_set[1].append(self.dataset[1][i])
            if self.test_set[2] != []:
                self.test_set[2].append(self.dataset[1][i])

        sampled=sorted(sampled)
        
        for i in range(len(sampled)):
            sampled[i]=sampled[i]-i
            if self.test_set[2] != []:
                self.test_set[2].pop(i)
        
        for i in sampled:
            self.dataset[0].pop(i)
            self.dataset[1].pop(i)
            if self.dataset[2] != []:
                self.dataset[2].pop(i)
            
    def merge(self,new_dataset, shift_factor, option='-'):
        '''Merges two Dataset objects together, generating a new Dataset object with pairs of data points from the two datasets merged in an unique instance.
        It will not make any dimensionality check for data consistency, so be careful, especially in giving datasets with the same number of instances.

        Parameters:
            One of the two Dataset objects to merge, an integer representing the shift, in absolute value, to perform to the indexes of the second dataset, 
            before merging it with the first one, and the sign of the shift to perform. 

        Returns: 
            Dataset object, that represents the merging of thhe two Dataset objects involved.
        '''
        merged_dataset= Dataset([],[],[],[],[],[])
        size = self.get_data_dim()
        data_merger = np.zeros((size[0],2*size[1],size[2]))
        label_merger = 0
        prep_merger = np.zeros((size[0],8))
                
        for i in range(new_dataset.get_size()):
            j = i - shift_factor
            if option=='-':
                data_merger[:,0:size[1],:] = self.dataset[0][i]
                data_merger[:,size[1]:,:] = new_dataset.dataset[0][j]
                label_merger = merged_dataset.select_case(self.dataset[1][i],new_dataset.dataset[1][j])
                if self.dataset[2] != []:
                    prep_merger[:,0:4] = self.dataset[2][i]
                    prep_merger[:,4:] = new_dataset.dataset[2][j]
                    merged_dataset.append_data(data_merger,label_merger,prep_merger)
                else:
                    merged_dataset.append_data(data_merger,label_merger)
                
            elif option=='+':
                data_merger[:,0:size[1],:] = self.dataset[0][j]
                data_merger[:,size[1]:,:] = new_dataset.dataset[0][i]
                label_merger = merged_dataset.select_case(self.dataset[1][j],new_dataset.dataset[1][i])
                if self.dataset[2] != []:
                    prep_merger[:,0:4] = self.dataset[2][j]
                    prep_merger[:,4:] = new_dataset.dataset[2][i]
                    merged_dataset.append_data(data_merger,label_merger,prep_merger)
                else:
                    merged_dataset.append_data(data_merger,label_merger)

        if self.test_set != []:
            size = self.get_data_dim()
            data_merger = np.zeros((size[0],2*size[1],size[2]))
            label_merger = 0
            prep_merger = np.zeros((size[0],8))
            shift_factor = int(self.get_test_size()/2) #This shift generates all possible pairs of the three devised classes
            
            for i in range(len(new_dataset.test_set[0])):
                j = i - shift_factor
                if option=='+':
                    data_merger[:,0:size[1],:] = self.test_set[0][i]
                    data_merger[:,size[1]:,:] = new_dataset.test_set[0][j]
                    label_merger = merged_dataset.select_case(self.test_set[1][i],new_dataset.test_set[1][j])
                    if self.test_set[2] != []:
                        prep_merger[:,0:4] = self.test_set[2][i]
                        prep_merger[:,4:] = new_dataset.test_set[2][j]
                        merged_dataset.append_test(data_merger,label_merger,prep_merger)
                    else:
                        merged_dataset.append_test(data_merger,label_merger)
                    
                elif option=='-':
                    data_merger[:,0:size[1],:] = self.test_set[0][j]
                    data_merger[:,size[1]:,:] = new_dataset.test_set[0][i]
                    label_merger = merged_dataset.select_case(self.test_set[1][j],new_dataset.test_set[1][i])
                    if self.test_set[2] != []:
                        prep_merger[:,0:4] = self.test_set[2][j]
                        prep_merger[:,4:] = new_dataset.test_set[2][i]
                        merged_dataset.append_test(data_merger,label_merger,prep_merger)
                    else:
                        merged_dataset.append_test(data_merger,label_merger)

        return merged_dataset
    
    def pop(self,set,indexes):
        '''Pops out elements of the training set or test set, according to what is specified.

        Parameters:
            A string representing the set to pop elements from, a list of the indexes of the elements to discard.

        Returns: 
            None.
        '''

        for i in range(len(indexes)):
            indexes[i]=indexes[i]-i

        if set == 'train':
            for index in indexes:
                self.dataset[0].pop(index)
                self.dataset[1].pop(index)
                self.dataset[2].pop(index)
        elif set == 'test':
            for index in indexes:
                self.test_set[0].pop(index)
                self.test_set[1].pop(index)
                self.test_set[2].pop(index)

    def save(self, filename=''):
        '''Saves the Dataset object in a pickle file format. It will be saved in the same path of where this method is called.

        Parameters:
            Name of the file where to store the data, that must include '.pickle' at the end

        Returns:
            None.
        
        '''
        with open(filename, "wb") as output:  # Overwrites any existing file. 
            pickle.dump([Dataset(data_points=self.dataset[0],labels=self.dataset[1],prep_data=self.dataset[2],
            test_set=self.test_set[0],test_labels=self.test_set[1],test_prep=self.test_set[2])], output)#It has to be done this way, otherwise pickle 
                                                                                                            #replaces the Dataset object with a list, 
                                                                                                            #losing all the built-in methods


    def select_case(self,label1, label2):
        '''Gives the merged data point a new label, by looking at the labels of the original data points merged.

        Parameters:
            The labels of the two original data points.

        Returns: 
            An integer representing the new label.
        '''
        if label1 == 1 and label2 == 1:
            return 1
        elif label1 ==1 and label2 ==2:
            return 2
        elif label1 ==1 and label2 ==3:
            return 3
        elif label1 ==2 and label2 ==1:
            return 4
        elif label1 ==2 and label2 ==2:
            return 5
        elif label1 ==2 and label2 ==3:
            return 6
        elif label1 ==3 and label2 ==1:
            return 7
        elif label1 ==3 and label2 ==2:
            return 8
        elif label1 ==3 and label2 ==3:
            return 9
    

    def unite(self,new_dataset):
        '''Unites two Dataset objects together, generating a new Dataset object with all the data points and labels of the two objects.
        It will not make any dimensionality check for data consistency, so be careful.

        Parameters:
            One of the two Dataset objects to unite.

        Returns: 
            Dataset object, that represents the union of thhe two Dataset objects involved.
        '''
        united_dataset= Dataset(self.dataset[0],self.dataset[1],self.dataset[2],self.test_set[0],self.test_set[1],self.test_set[2])
        if united_dataset.get_size()!=0:
            for i in range(len(new_dataset.dataset[0])):
                united_dataset.dataset[0].append(new_dataset.dataset[0][i])
                united_dataset.dataset[1].append(new_dataset.dataset[1][i])
                if united_dataset.dataset[2] != []:
                    united_dataset.dataset[2].append(new_dataset.dataset[2][i])

        
        if united_dataset.get_test_size()!=0:
            for i in range(len(new_dataset.test_set[1])):
                united_dataset.dataset[0].append(new_dataset.test_set[0][i])
                united_dataset.dataset[1].append(new_dataset.test_set[1][i])
                if united_dataset.dataset[2] != []:
                    united_dataset.dataset[2].append(new_dataset.test_set[2][i])

        return united_dataset

    
