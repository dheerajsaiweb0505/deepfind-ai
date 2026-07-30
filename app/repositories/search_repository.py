from app.models.search_history import SearchHistory


class SearchRepository:

    @staticmethod
    def save(
        db,
        query,
        user_id
    ):

        history = SearchHistory(
            query=query,
            user_id=user_id
        )

        db.add(history)

        db.commit()

        db.refresh(history)

        return history

    @staticmethod
    def recent(
        db,
        user_id,
        limit=10
    ):

        return (

            db.query(SearchHistory)

            .filter(
                SearchHistory.user_id == user_id
            )

            .order_by(
                SearchHistory.created_at.desc()
            )

            .limit(limit)

            .all()

        )