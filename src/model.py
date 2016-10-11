import tflearn
import sys
import numpy as np

class supersample_generator(tflearn.SequenceGenerator):

   '''
   Builds off tflearn.SequenceGenerator to sample in parallel.
   '''
    
   def generate(self, seq_length, temperature=0.5, seq_seeds=None,
                 display=False,batch_streams=1):

        assert(len(seq_seeds) == batch_streams)
       
        sequence       = seq_seeds[:]
        whole_sequence = seq_seeds[:]

        for i in range(seq_length):
            
            x = np.zeros((batch_streams, self.seq_maxlen, len(self.dic)))

            for j in range(batch_streams):
                for t, char in enumerate(sequence[j]):
                    x[j, t, self.dic[char]] = 1.

            preds = self._predict(x)

            for j in range(batch_streams):
                next_index = _sample(preds[j], temperature)
                next_char = self.rev_dic[next_index]

                sequence[j] = sequence[j][1:] + next_char                
                whole_sequence[j] += next_char

            #if display:
            #    sys.stdout.write(next_char)
            #    sys.stdout.flush()

        #if display: print()

        return whole_sequence

def build_model(char_idx, maxlen,
                layer_size=128,
                checkpoint_path='model',):

    g = tflearn.input_data(shape=[None, maxlen, len(char_idx)])
    g = tflearn.lstm(g, layer_size, return_seq=True)
    g = tflearn.dropout(g, 0.5)
    g = tflearn.lstm(g, layer_size)
    g = tflearn.dropout(g, 0.5)
    g = tflearn.fully_connected(g, len(char_idx), activation='softmax')
    g = tflearn.regression(g,
                           optimizer='adam',
                           loss='categorical_crossentropy',
                           learning_rate=0.001
    )

    m = supersample_generator(g,
                              dictionary=char_idx,
                              seq_maxlen=maxlen,
                              clip_gradients=5.0,
                              checkpoint_path=checkpoint_path)
    return m

def _sample(a, temperature=1.0):
    ''' Same as tflearn.models.generator._sample '''
    a = np.log(a) / temperature
    a = np.exp(a) / np.sum(np.exp(a))
    p = np.argmax(np.random.multinomial(1, a, 1))
    return p
