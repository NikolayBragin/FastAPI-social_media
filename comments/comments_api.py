from fastapi import Body
from datetime import datetime

from comments import comment_router
from database.commentservice import grt_exact_post_comment_db, add_new_comment_db, delete_exact_comment_db, change_exact_comment_db

# запрос на поучение комментария к посту
@comment_router.get('/post-comment')
async def get_exact_post_comment(post_id: int):
    result = grt_exact_post_comment_db(post_id)

    return {'status': 1, 'message': result}

# запрос на добавление комментария (Body)
@comment_router.post('/add-comment')
async def add_new_comment(post_id: int = Body(...), user_id: int = Body(...), comment_text: str = Body(...)):
    result = add_new_comment_db(post_id=post_id, user_id=user_id, comment_text=comment_text, publish_date=datetime.now())

    return {'status': 1, 'message': result}

# Запрос на изменение текста к комментарию
@comment_router.put('/edit-comment')
async def edit_exact_comment(comment_id: int = Body(...), new_comment_text: str = Body(...)):
    result = change_exact_comment_db(comment_id=comment_id, new_comment_text=new_comment_text)

    return {'status': 1, 'message': result}

# удаление определенного комментария
@comment_router.delete('/delete-comment')
async def delete_exact_comment(comment_id: int):
    result = change_exact_comment_db(comment_id=comment_id)

    return {'status': 1, 'message': result}