from collections import defaultdict
import heapq

class AutoCompleteSystem:
    def __init__(self, sentences, times):
        # Dictionary to store sentence and its frequency
        self.sentence_frequency = defaultdict(int)
        for sentence, time in zip(sentences, times):
            self.sentence_frequency[sentence] += time
        self.current_sentence = ""  # To store the user's current input

    def input(self, c):
        # If we encounter the special character '#', save the current sentence
        if c == '#':
            self.sentence_frequency[self.current_sentence] += 1  # Update or add the current sentence
            self.current_sentence = ""  # Reset for the next sentence
            return []  # Return an empty list after storing the sentence

        # Otherwise, keep adding characters to the current sentence
        self.current_sentence += c

        # Find all sentences that match the current prefix (self.current_sentence)
        matches = []
        for sentence in self.sentence_frequency:
            if sentence.startswith(self.current_sentence):
                # Add (-frequency, sentence) to sort by frequency first, then lexicographically
                matches.append((-self.sentence_frequency[sentence], sentence))

        # Sort the matches: first by frequency, then lexicographically if frequencies are equal
        heapq.heapify(matches)
        top_3 = []
        for _ in range(min(3, len(matches))):
            top_3.append(heapq.heappop(matches)[1])  # Extract the sentence

        return top_3


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n = int(input())
        sentences = []
        times = []
        for _ in range(n):
            sentence = input()
            sentences.append(sentence)
            time = int(input())
            times.append(time)

        obj = AutoCompleteSystem(sentences, times)

        q = int(input())
        for _ in range(q):
            query = input()
            qq = ""
            for x in query:
                qq += x
                suggestions = obj.input(x)
                if x == '#':
                    continue
                print('Typed : "' + qq + '" , Suggestions:')
                for y in suggestions:
                    print(y)

        t -= 1

# } Driver Code Ends
