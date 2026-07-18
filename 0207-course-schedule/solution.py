class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = prerequisites


        graph = defaultdict(list)

        for course, prereq in courses:
            graph[course].append(prereq)
            #print("first for ->  course: ", course,"and pre: ",prereq)
        
        #print(graph)
        #print(courses)

    
        NOT_VISITED = 0
        VISITING = 1
        VISITED = 2

        states = [NOT_VISITED] * numCourses

        def dfs(course): # va verifica daca materia aia poate fi nu fi facuta
        
            if states[course] == 2: return True # adica a fost vizitat si poate fi facuta materia
            if states[course] == 1: return False # adica e inca viziting si trecem a doua oara 
                                                #  pe la ea deci va returna False ca e un loop
            
            states[course] = 1 # daca nu e loop, atunci ii vom da 1 ca abia acum e VISITING

            for prereq in graph[course]: # la forul cu for course am ales cursul si aici prereq la curs
                if not dfs(prereq): return False # Daca la dfs daca avem False -> nu poate fi facuta 
                                                 # deci va returna False
            
            states[course] = 2
            return True



        for course in range(numCourses):
            if not dfs(course): return False # Daca la dfs daca avem False -> nu poate fi facuta 
                                             # deci va returna False

        return True
