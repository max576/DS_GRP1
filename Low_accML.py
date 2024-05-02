import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text

bert_prep = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3")
bert_enc = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4")
def build_model():
    bert_input = tf.keras.layers.Input(shape = (), dtype = tf.string, name='text_bert')
    prep_text = bert_prep(bert_input)
    output = bert_enc(prep_text)
    pooled_output = tf.keras.layers.concatenate(
        tuple([output['enc_outputs'][i] for i in range(-4, 0)]), 
        name = 'last_4_hidden_states',
        axis = -1
    )[:, 0, :]
    pooled_output = tf.keras.layers.LayerNormalization()(pooled_output)
    Dense = tf.keras.layers.Dropout(0.5)(pooled_output)
    Dense = tf.keras.layers.Dense(768, activation='relu')(Dense)
    Dense = tf.keras.layers.Dropout(0.5)(Dense)
    classifer = tf.keras.layers.Dense(3,activation='softmax', name="output")(Dense)
    model = tf.keras.m
model = build_model()
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5),
              loss='categorical_crossentropy',
              metrics=['accuracy'])
h = model.fit(X_train, y_train, 
              epochs=80, 
              validation_data=(X_test, y_test),
              callbacks = [early_stopping,check_point])
