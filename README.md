Tablas

1. *Usuarios (Users)*
   - user_id: INT, PRIMARY KEY, AUTO_INCREMENT
   - username: VARCHAR(50), UNIQUE, NOT NULL
   - email: VARCHAR(100), UNIQUE, NOT NULL
   - password: VARCHAR(255), NOT NULL
   - created_at: DATETIME, NOT NULL, DEFAULT CURRENT_TIMESTAMP

2. *Categorías (Categories)*
   - category_id: INT, PRIMARY KEY, AUTO_INCREMENT
   - category_name: VARCHAR(100), NOT NULL
   - description: TEXT
   - created_at: DATETIME, NOT NULL, DEFAULT CURRENT_TIMESTAMP

3. *Hilos (Threads)*
   - thread_id: INT, PRIMARY KEY, AUTO_INCREMENT
   - title: VARCHAR(255), NOT NULL
   - content: TEXT, NOT NULL
   - user_id: INT, FOREIGN KEY (References Usuarios.user_id), NOT NULL
   - category_id: INT, FOREIGN KEY (References Categorías.category_id), NOT NULL
   - created_at: DATETIME, NOT NULL, DEFAULT CURRENT_TIMESTAMP
   - updated_at: DATETIME, NULL

4. *Comentarios (Posts)*
   - post_id: INT, PRIMARY KEY, AUTO_INCREMENT
   - content: TEXT, NOT NULL
   - user_id: INT, FOREIGN KEY (References Usuarios.user_id), NOT NULL
   - thread_id: INT, FOREIGN KEY (References Hilos.thread_id), NOT NULL
   - created_at: DATETIME, NOT NULL, DEFAULT CURRENT_TIMESTAMP
   - updated_at: DATETIME, NULL

5. *Etiquetas (Tags)*
   - tag_id: INT, PRIMARY KEY, AUTO_INCREMENT
   - tag_name: VARCHAR(50), UNIQUE, NOT NULL

6. *Etiquetas de Hilos (Thread_Tags)*
   - thread_id: INT, FOREIGN KEY (References Hilos.thread_id), PRIMARY KEY
   - tag_id: INT, FOREIGN KEY (References Etiquetas.tag_id), PRIMARY KEY

7. *Votos (Votes)*
   - vote_id: INT, PRIMARY KEY, AUTO_INCREMENT
   - user_id: INT, FOREIGN KEY (References Usuarios.user_id), NOT NULL
   - post_id: INT, FOREIGN KEY (References Comentarios.post_id), NOT NULL
   - vote_type: ENUM('upvote', 'downvote'), NOT NULL
   - created_at: DATETIME, NOT NULL, DEFAULT CURRENT_TIMESTAMP

8. *Imágenes (Images)*
   - image_id: INT, PRIMARY KEY, AUTO_INCREMENT
   - image_url: VARCHAR(255), NOT NULL
   - uploaded_at: DATETIME, NOT NULL, DEFAULT CURRENT_TIMESTAMP

9. *Imágenes de Hilos (Thread_Images)*
   - thread_id: INT, FOREIGN KEY (References Hilos.thread_id), PRIMARY KEY
   - image_id: INT, FOREIGN KEY (References Imágenes.image_id), PRIMARY KEY

10. *Imágenes de Comentarios (Post_Images)*
    - post_id: INT, FOREIGN KEY (References Comentarios.post_id), PRIMARY KEY
    - image_id: INT, FOREIGN KEY (References Imágenes.image_id), PRIMARY KEY

### Relaciones

1. Un *Usuario* puede crear múltiples *Hilos*.
2. Un *Usuario* puede crear múltiples *Comentarios*.
3. Un *Hilo* pertenece a una única *Categoría*.
4. Un *Hilo* puede tener múltiples *Comentarios*.
5. Un *Comentario* pertenece a un único *Hilo*.
6. Un *Hilo* puede tener múltiples *Etiquetas* a través de la tabla intermedia *Thread_Tags*.
7. Un *Usuario* puede votar múltiples *Comentarios* y un *Comentario* puede tener múltiples *Votos*.
8. Un *Hilo* puede tener múltiples *Imágenes* a través de la tabla intermedia *Thread_Images*.
9. Un *Comentario* puede tener múltiples *Imágenes* a través de la tabla intermedia *Post_Images*.

### Diagrama Entidad-Relación (ER)

Puedes visualizar este modelo mediante un diagrama ER simple como el siguiente:


Usuarios (User)
| user_id | username | email | password | created_at |

Categorías (Category)
| category_id | category_name | description | created_at |

Hilos (Thread)
| thread_id | title | content | user_id | category_id | created_at | updated_at |

Comentarios (Post)
| post_id | content | user_id | thread_id | created_at | updated_at |

Etiquetas (Tag)
| tag_id | tag_name |

Thread_Tags
| thread_id | tag_id |

Votos (Vote)
| vote_id | user_id | post_id | vote_type | created_at |

Imágenes (Image)
| image_id | image_url | uploaded_at |

Thread_Images
| thread_id | image_id |

Post_Images
| post_id | image_id |


Este modelo actualizado permite la publicación de imágenes tanto en hilos como en comentarios, manteniendo una estructura clara y relaciones adecuadas entre las entidades.
