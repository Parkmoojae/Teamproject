from datasource import session
from sqlalchemy import text, exc, and_, or_, func, String, DateTime, bindparam, Integer, VARCHAR
import uuid, datetime
from dto.model import Board, BoardList

def selectBoard(data):

        # queryResult = session.query(Board, BoardList).\
        #     with_entities(Board.board_id, Board.board_content, Board.board_del,Board.board_regdate,Board.board_title,\
        #     BoardList.board_list_name,Board.board_pid,Board.user_id).\
        #     filter(Board.board_list_id == BoardList.board_list_id).all()

        
        query="""
        with recursive cte as
        (
        select     board_id,
            board_title,
            board_content,
            user_id,
            board_pid,
            board_list_id,
            board_del,
            board_regdate,
            0 AS depth,
            CAST(LPAD(board_id, 10, "0") AS VARCHAR(1000)) as lvl,
            CAST(LPAD(board_id, 10, "0") AS VARCHAR(1000)) as lvl2
        from       board
        where      board_pid = 0
        union all
        select     r.board_id,
            r.board_title,
            r.board_content,
            r.user_id,
            r.board_pid,
            r.board_list_id,
            r.board_del,
            r.board_regdate,
            1 + depth AS depth,
            lvl as lvl,
            CONCAT(cte.lvl2, "-", LPAD(r.board_id, 10, "0")) as lvl2
        from       board r
        inner join cte
            on r.board_pid = cte.board_id
        )
        SELECT * FROM
        (
        select @rownum:=@rownum+1 b_num,c.* 
		  FROM cte c,(SELECT @rownum:=0) f
		  WHERE board_list_id=:board_list_id
		  ORDER BY c.board_id
		  
        ) d
        INNER JOIN user
        ON d.user_id = user.user_id
        ORDER BY lvl DESC,lvl2  
        """

        stmt = text(query)
        stmt = stmt.bindparams(bindparam("board_list_id", type_=Integer))
        queryResult = session.execute(stmt,{"board_list_id":data})
        print("@@@@@@@@@@@@@@@@@@@")
        print(queryResult)


        result = [{column: value for column, value in rowproxy.items() }for rowproxy in queryResult]
        

        # result = []
        # for row in queryResult:
        #     result.append(row._asdict())
        print(result)
        print("@@@@@@@@@@@@@@@@@@@@@@@")
        return result
