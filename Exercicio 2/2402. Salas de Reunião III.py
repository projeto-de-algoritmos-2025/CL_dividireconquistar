class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        ocupadas = []        
        livres = list(range(n))       
        heapify(livres)     
        contador = [0] * n       
        for inicio, fim in meetings:
            while ocupadas and ocupadas[0][0] <= inicio:
                heappush(livres, heappop(ocupadas)[1])           
            if livres:
                i = heappop(livres)
                contador[i] += 1
                heappush(ocupadas, (fim, i))
            else:
                tempo_termino, i = heappop(ocupadas)
                contador[i] += 1
                heappush(ocupadas, (tempo_termino + fim - inicio, i))
        
        resposta = 0
        for i, valor in enumerate(contador):
            if valor > contador[resposta] or (valor == contador[resposta] and i < resposta):
                resposta = i
        return resposta
